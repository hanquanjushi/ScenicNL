from pinecone import Pinecone

pc = Pinecone(api_key="pcsk_gHxda_Noo9fHyo28mo64W2JW4znc9HEWThLz3WwVaZW6QSbKYiQhJmF3WEoAVogbjwTB")
index = pc.Index("quickstart")
index.upsert(
    vectors=[
        {
            "id": "vec1", 
            "values": [1.0, 1.5], 
            "metadata": {"genre": "drama"}
        }, {
            "id": "vec2", 
            "values": [2.0, 1.0], 
            "metadata": {"genre": "action"}
        }, {
            "id": "vec3", 
            "values": [0.1, 0.3], 
            "metadata": {"genre": "drama"}
        }, {
            "id": "vec4", 
            "values": [1.0, -2.5], 
            "metadata": {"genre": "action"}
        }
    ],
    namespace= "ns1"
)
response = index.query(
    namespace="ns1",
    vector=[0.1, 0.3],
    top_k=2,
    include_values=True,
    include_metadata=True,
    filter={"genre": {"$eq": "action"}}
)
    
print(response)