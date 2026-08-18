import pandas as pd
import os


# ============================================================
# Australian Travel Assistant - Walert Test Dataset
# ============================================================
#
# This script manually defines:
#   1. Test questions
#   2. Relevant passages
#   3. Ground-truth question-to-passage mappings
#
# It then creates:
#   data/topics.csv
#   data/groundtruth.csv
#   data/collection.csv
#
# Source:
# Australian Government
# travelling-returning-australia-english.pdf
# ============================================================


# ------------------------------------------------------------
# 1. CREATE OUTPUT FOLDER
# ------------------------------------------------------------

OUTPUT_FOLDER = "data"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)


# ------------------------------------------------------------
# 2. TEST QUESTIONS
# ------------------------------------------------------------

questions = [
    {
        "qid": "Q001",
        "question": "What goods must travellers declare before arriving in Australia?"
    },
    {
        "qid": "Q002",
        "question": "What should travellers do with food left over from their plane or ship?"
    },
    {
        "qid": "Q003",
        "question": "What steps should travellers follow when they arrive in Australia?"
    },
    {
        "qid": "Q004",
        "question": "Can travellers' bags be checked even if they do not declare any goods?"
    },
    {
        "qid": "Q005",
        "question": "What can happen if a traveller fails to declare biosecurity risk goods?"
    },
    {
        "qid": "Q006",
        "question": "Will travellers be penalised if they declare goods that are not allowed into Australia?"
    },
    {
        "qid": "Q007",
        "question": "What happens to goods that a traveller declares when entering Australia?"
    },
    {
        "qid": "Q008",
        "question": "Do travellers need to be concerned about contaminated hiking boots or outdoor equipment?"
    },
    {
        "qid": "Q009",
        "question": "What should a traveller do if they discover a biosecurity risk after arriving in Australia?"
    },
    {
        "qid": "Q010",
        "question": "Are laptops, phones and cameras considered biosecurity risks?"
    },
    {
        "qid": "Q011",
        "question": "Do travellers need to declare dairy and egg products when entering Australia?"
    },
    {
        "qid": "Q012",
        "question": "What types of plant material may need to be declared when entering Australia?"
    },
    {
        "qid": "Q013",
        "question": "Do travellers need to declare herbs, spices or herbal teas when entering Australia?"
    },
    {
        "qid": "Q014",
        "question": "What animal products may need to be declared when travelling to Australia?"
    },
    {
        "qid": "Q015",
        "question": "How can travellers check whether goods are allowed into Australia before travelling?"
    }
]


# ------------------------------------------------------------
# 3. PASSAGES FROM SOURCE DOCUMENT
# ------------------------------------------------------------

passages = [
    {
        "passage_id": "P001",
        "passage": (
            "Complete your declaration. By law, you must declare any risk "
            "goods, including certain food, plant material and animal products."
        ),
        "source": "travelling-returning-australia-english.pdf",
        "page": 1
    },

    {
        "passage_id": "P002",
        "passage": (
            "Don't take food off the plane or ship."
        ),
        "source": "travelling-returning-australia-english.pdf",
        "page": 1
    },

    {
        "passage_id": "P003",
        "passage": (
            "When you arrive in Australia, proceed through immigration "
            "clearance, collect your baggage, then proceed to biosecurity "
            "inspection and present your declaration and the goods you are "
            "declaring to the biosecurity officer."
        ),
        "source": "travelling-returning-australia-english.pdf",
        "page": 1
    },

    {
        "passage_id": "P004",
        "passage": (
            "Your bags may be checked by a biosecurity officer, a detector "
            "dog or X-ray, even if you don't declare any goods."
        ),
        "source": "travelling-returning-australia-english.pdf",
        "page": 1
    },

    {
        "passage_id": "P005",
        "passage": (
            "If you provide false or misleading information to a biosecurity "
            "officer or on your declaration, fail to answer questions about "
            "the goods, or fail to comply with directions, you may be given "
            "an infringement notice, be subject to civil penalty proceedings, "
            "and/or be prosecuted for a criminal offence."
        ),
        "source": "travelling-returning-australia-english.pdf",
        "page": 1
    },

    {
        "passage_id": "P006",
        "passage": (
            "You will not be penalised under the Biosecurity Act 2015 if you "
            "declare and present all goods, even if they are not allowed into "
            "Australia."
        ),
        "source": "travelling-returning-australia-english.pdf",
        "page": 1
    },

    {
        "passage_id": "P007",
        "passage": (
            "A biosecurity officer will inspect your presented goods and may "
            "ask for more information or documentation. If the goods are "
            "permitted and pass inspection they will be returned to you. "
            "If the goods do not pass inspection, you may have to pay to "
            "have the goods treated, exported from Australia or destroyed."
        ),
        "source": "travelling-returning-australia-english.pdf",
        "page": 1
    },

    {
        "passage_id": "P008",
        "passage": (
            "Outdoor, camping and sports equipment and footwear can be a "
            "biosecurity concern. Examples include hiking boots, fishing "
            "equipment and anything that could be contaminated with soil, "
            "seeds, animal or faecal matter, or freshwater."
        ),
        "source": "travelling-returning-australia-english.pdf",
        "page": 2
    },

    {
        "passage_id": "P009",
        "passage": (
            "If you find live animals, insects, soil, plant material or other "
            "risk items when unpacking, phone 1800 798 636. "
            "You won't be penalised."
        ),
        "source": "travelling-returning-australia-english.pdf",
        "page": 2
    },

    {
        "passage_id": "P010",
        "passage": (
            "Electronic equipment including laptops, tablets, phones and "
            "cameras is not considered a biosecurity risk."
        ),
        "source": "travelling-returning-australia-english.pdf",
        "page": 2
    },

    {
        "passage_id": "P011",
        "passage": (
            "Dairy and egg products are examples of goods that may need to "
            "be declared. These include infant formula, cheese, milk, yoghurt, "
            "eggs, mayonnaise, noodles and pasta."
        ),
        "source": "travelling-returning-australia-english.pdf",
        "page": 2
    },

    {
        "passage_id": "P012",
        "passage": (
            "Plant material that may need to be declared includes live plants, "
            "seeds, bulbs, cuttings, fresh and dried flowers, wooden items, "
            "bark, leaves and straw."
        ),
        "source": "travelling-returning-australia-english.pdf",
        "page": 2
    },

    {
        "passage_id": "P013",
        "passage": (
            "Food items that may need to be declared include honey, herbs "
            "and spices, including herbal teas and medicines, snacks and "
            "other foods."
        ),
        "source": "travelling-returning-australia-english.pdf",
        "page": 2
    },

    {
        "passage_id": "P014",
        "passage": (
            "Animal products that may need to be declared include eggs, nests, "
            "feathers, bones, horns, skins, animal fur or hair, stuffed animals, "
            "shells, coral and bee products."
        ),
        "source": "travelling-returning-australia-english.pdf",
        "page": 2
    },

    {
        "passage_id": "P015",
        "passage": (
            "Travellers can check Australian Government information about "
            "bringing goods into Australia and use BICON to check import "
            "conditions. If an import permit is required, it must be obtained "
            "before bringing the goods into Australia."
        ),
        "source": "travelling-returning-australia-english.pdf",
        "page": 1
    }
]


# ------------------------------------------------------------
# 4. GROUND TRUTH
# ------------------------------------------------------------
#
# This tells the evaluation system which passage is considered
# relevant for each test question.
#
# Example:
# Q001 -> P001
# ------------------------------------------------------------

groundtruth = [
    {"qid": "Q001", "passage_id": "P001"},
    {"qid": "Q002", "passage_id": "P002"},
    {"qid": "Q003", "passage_id": "P003"},
    {"qid": "Q004", "passage_id": "P004"},
    {"qid": "Q005", "passage_id": "P005"},
    {"qid": "Q006", "passage_id": "P006"},
    {"qid": "Q007", "passage_id": "P007"},
    {"qid": "Q008", "passage_id": "P008"},
    {"qid": "Q009", "passage_id": "P009"},
    {"qid": "Q010", "passage_id": "P010"},
    {"qid": "Q011", "passage_id": "P011"},
    {"qid": "Q012", "passage_id": "P012"},
    {"qid": "Q013", "passage_id": "P013"},
    {"qid": "Q014", "passage_id": "P014"},
    {"qid": "Q015", "passage_id": "P015"}
]


# ------------------------------------------------------------
# 5. CONVERT TO PANDAS DATAFRAMES
# ------------------------------------------------------------

topics_df = pd.DataFrame(questions)

collection_df = pd.DataFrame(passages)

groundtruth_df = pd.DataFrame(groundtruth)


# ------------------------------------------------------------
# 6. BASIC VALIDATION
# ------------------------------------------------------------

print("Checking dataset...")

# Check duplicate question IDs
if topics_df["qid"].duplicated().any():
    raise ValueError("Duplicate question IDs found.")

# Check duplicate passage IDs
if collection_df["passage_id"].duplicated().any():
    raise ValueError("Duplicate passage IDs found.")

# Check that every ground-truth question exists
valid_question_ids = set(topics_df["qid"])

for qid in groundtruth_df["qid"]:
    if qid not in valid_question_ids:
        raise ValueError(
            f"Ground-truth question {qid} does not exist in topics."
        )

# Check that every ground-truth passage exists
valid_passage_ids = set(collection_df["passage_id"])

for passage_id in groundtruth_df["passage_id"]:
    if passage_id not in valid_passage_ids:
        raise ValueError(
            f"Ground-truth passage {passage_id} "
            f"does not exist in collection."
        )

print("Dataset validation successful.")


# ------------------------------------------------------------
# 7. CREATE topics.csv
# ------------------------------------------------------------

topics_path = os.path.join(
    OUTPUT_FOLDER,
    "topics.csv"
)

topics_df.to_csv(
    topics_path,
    index=False,
    encoding="utf-8"
)

print(f"Created: {topics_path}")


# ------------------------------------------------------------
# 8. CREATE groundtruth.csv
# ------------------------------------------------------------

groundtruth_path = os.path.join(
    OUTPUT_FOLDER,
    "groundtruth.csv"
)

groundtruth_df.to_csv(
    groundtruth_path,
    index=False,
    encoding="utf-8"
)

print(f"Created: {groundtruth_path}")


# ------------------------------------------------------------
# 9. CREATE collection.csv
# ------------------------------------------------------------

collection_path = os.path.join(
    OUTPUT_FOLDER,
    "collection.csv"
)

collection_df.to_csv(
    collection_path,
    index=False,
    encoding="utf-8"
)

print(f"Created: {collection_path}")


# ------------------------------------------------------------
# 10. SUMMARY
# ------------------------------------------------------------

print()
print("=" * 50)
print("Walert travel dataset created successfully!")
print("=" * 50)

print(f"Questions: {len(topics_df)}")
print(f"Passages: {len(collection_df)}")
print(f"Ground-truth mappings: {len(groundtruth_df)}")

print()
print("Files created:")
print(topics_path)
print(groundtruth_path)
print(collection_path)