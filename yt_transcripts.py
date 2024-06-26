import logging

from youtube_transcript_api import YouTubeTranscriptApi

logging.root.setLevel(logging.INFO)
logger = logging.getLogger(__name__)


def get_transcript(video_id: str) -> list:
    logger.info(f"Getting transcript for video id: {video_id}")
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=["en"])
        logger.info(
            f"Transcript for video id: {video_id} with length {len(transcript)} \
                     fetched successfully"
        )
        return transcript
    except Exception as e:
        logger.error(f"Error while fetching transcript for video id: {video_id}")
        logger.error(e)
        raise Exception(f"Error while fetching transcript for video id: {video_id}")
