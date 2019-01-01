VIDEOS_DIR := data/originals
METADATA_DIR := data/metadata
THUMBNAILS_DIR := data/thumbnails
VIDEOS := $(wildcard $(VIDEOS_DIR)/*.mp4)
METADATAS := $(VIDEOS:$(VIDEOS_DIR)/%.mp4=$(METADATA_DIR)/%.json)
THUMBNAILS := $(VIDEOS:$(VIDEOS_DIR)/%.mp4=$(THUMBNAILS_DIR)/%)

$(METADATA_DIR)/%.json: $(VIDEOS_DIR)/%.mp4
	./extract_scenes $< $@

$(THUMBNAILS_DIR)/%: $(METADATA_DIR)/%.json $(VIDEOS_DIR)/%.mp4
	./extract_thumbnails $^ $(THUMBNAILS_DIR)

index.html: $(METADATAS) $(THUMBNAILS)
	./generate_html $(METADATA_DIR) $(THUMBNAILS_DIR) index.html.mako index.html

test:
	python3 -m unittest
