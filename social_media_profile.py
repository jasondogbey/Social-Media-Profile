class UserProfile:
    def __init__(self, name, username, email):
        self.name = name
        self.username = username
        self.email = email
        self.posts = []
        self.comments = []
    
    def create_post(self, content):
        new_post = Post(content, self)
        self.posts.append(new_post)
        return new_post
    
    def add_comment(self, post, text):
        new_comment = Comment(text, self)
        post.add_comment(new_comment)
        self.comments.append(new_comment)


class Post:
    def __init__(self, content, author):
        self.content = content
        self.author = author
        self.comments = []
        
    def add_comment(self, comment):
        self.comments.append(comment)
    

class Comment:
    def __init__(self, text, author):
        self.text = text
        self.author = author


# Creating users
user1 = UserProfile("Jay", "user1", "user1@example.com")
user2 = UserProfile("Ye", "user2", "user2@example.com")

# User1 creates a post
post1 = user1.create_post("Hello, this is my first post!")

# User2 comments on post1
user2.add_comment(post1, "Nice post!")

# Display post content, author, and comments
print("Post Content:", post1.content)
print("Author:", post1.author.username)
print("Comments:")
for comment in post1.comments:
    print(f"{comment.author.username}: {comment.text}")