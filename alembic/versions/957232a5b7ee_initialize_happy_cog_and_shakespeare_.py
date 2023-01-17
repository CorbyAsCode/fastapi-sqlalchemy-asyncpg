"""initialize happy_cog and shakespeare tables

Revision ID: 957232a5b7ee
Revises: 
Create Date: 2022-06-04 13:02:45.839649

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "957232a5b7ee"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "nonsense",
        sa.Column(
            "id", postgresql.UUID(as_uuid=True), autoincrement=True, nullable=True
        ),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("name"),
        sa.UniqueConstraint("id"),
        sa.UniqueConstraint("name"),
        schema="happy_hog",
    )
    op.create_table(
        "stuff",
        sa.Column(
            "id", postgresql.UUID(as_uuid=True), autoincrement=True, nullable=True
        ),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("name"),
        sa.UniqueConstraint("id"),
        sa.UniqueConstraint("name"),
        schema="happy_hog",
    )
    op.create_table(
        "character",
        sa.Column("id", sa.String(length=32), nullable=False),
        sa.Column("name", sa.String(length=64), nullable=False),
        sa.Column("speech_count", sa.Integer(), nullable=False),
        sa.Column("abbrev", sa.String(length=32), nullable=True),
        sa.Column("description", sa.String(length=2056), nullable=True),
        sa.PrimaryKeyConstraint("id", name="character_pkey"),
        schema="shakespeare",
    )
    op.create_table(
        "wordform",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("plain_text", sa.String(length=64), nullable=False),
        sa.Column("phonetic_text", sa.String(length=64), nullable=False),
        sa.Column("stem_text", sa.String(length=64), nullable=False),
        sa.Column("occurences", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id", name="wordform_pkey"),
        schema="shakespeare",
    )
    op.create_table(
        "work",
        sa.Column("id", sa.String(length=32), nullable=False),
        sa.Column("title", sa.String(length=32), nullable=False),
        sa.Column("long_title", sa.String(length=64), nullable=False),
        sa.Column("year", sa.Integer(), nullable=False),
        sa.Column("genre_type", sa.String(length=1), nullable=False),
        sa.Column("source", sa.String(length=16), nullable=False),
        sa.Column("total_words", sa.Integer(), nullable=False),
        sa.Column("total_paragraphs", sa.Integer(), nullable=False),
        sa.Column("notes", sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint("id", name="work_pkey"),
        schema="shakespeare",
    )
    op.create_table(
        "chapter",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("work_id", sa.String(length=32), nullable=False),
        sa.Column("section_number", sa.Integer(), nullable=False),
        sa.Column("chapter_number", sa.Integer(), nullable=False),
        sa.Column("description", sa.String(length=256), nullable=False),
        sa.ForeignKeyConstraint(
            ["work_id"], ["shakespeare.work.id"], name="chapter_work_id_fkey"
        ),
        sa.PrimaryKeyConstraint("id", name="chapter_pkey"),
        sa.UniqueConstraint(
            "work_id",
            "section_number",
            "chapter_number",
            name="chapter_work_id_section_number_chapter_number_key",
        ),
        schema="shakespeare",
    )
    op.create_table(
        "character_work",
        sa.Column("character_id", sa.String(length=32), nullable=False),
        sa.Column("work_id", sa.String(length=32), nullable=False),
        sa.ForeignKeyConstraint(
            ["character_id"],
            ["shakespeare.character.id"],
            name="character_work_character_id_fkey",
        ),
        sa.ForeignKeyConstraint(
            ["work_id"], ["shakespeare.work.id"], name="character_work_work_id_fkey"
        ),
        sa.PrimaryKeyConstraint("character_id", "work_id", name="character_work_pkey"),
        schema="shakespeare",
    )
    op.create_table(
        "paragraph",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("work_id", sa.String(length=32), nullable=False),
        sa.Column("paragraph_num", sa.Integer(), nullable=False),
        sa.Column("character_id", sa.String(length=32), nullable=False),
        sa.Column("plain_text", sa.Text(), nullable=False),
        sa.Column("phonetic_text", sa.Text(), nullable=False),
        sa.Column("stem_text", sa.Text(), nullable=False),
        sa.Column("paragraph_type", sa.String(length=1), nullable=False),
        sa.Column("section_number", sa.Integer(), nullable=False),
        sa.Column("chapter_number", sa.Integer(), nullable=False),
        sa.Column("char_count", sa.Integer(), nullable=False),
        sa.Column("word_count", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["character_id"],
            ["shakespeare.character.id"],
            name="paragraph_character_id_fkey",
        ),
        sa.ForeignKeyConstraint(
            ["work_id", "section_number", "chapter_number"],
            [
                "shakespeare.chapter.work_id",
                "shakespeare.chapter.section_number",
                "shakespeare.chapter.chapter_number",
            ],
            name="paragraph_chapter_fkey",
        ),
        sa.ForeignKeyConstraint(
            ["work_id"], ["shakespeare.work.id"], name="paragraph_work_id_fkey"
        ),
        sa.PrimaryKeyConstraint("id", name="paragraph_pkey"),
        schema="shakespeare",
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("paragraph", schema="shakespeare")
    op.drop_table("character_work", schema="shakespeare")
    op.drop_table("chapter", schema="shakespeare")
    op.drop_table("work", schema="shakespeare")
    op.drop_table("wordform", schema="shakespeare")
    op.drop_table("character", schema="shakespeare")
    op.drop_table("stuff", schema="happy_hog")
    op.drop_table("nonsense", schema="happy_hog")
    # ### end Alembic commands ###
