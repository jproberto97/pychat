import openai

def main():
    print("Welcome to PychatV.1 Client!\n")

    x = "yes"
    while x == "yes":
        try:
            query = input("Input: ")

            # print(f"Query: {query}")

            completion = openai.Completion.create(engine="text-davinci-003", prompt=query, max_tokens=4000)

            output = completion.choices[0].text

            print(f"Output: {output}")

        except Exception as e:
            print(e)

        x = input("Ask other? [yes / no] :")



if __name__ == "__main__":
    main()