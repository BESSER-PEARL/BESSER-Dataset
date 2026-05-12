





import java.util.List;
import java.util.ArrayList;

public class Page  {

    private String Name;
    private String Description;
    private int ID_Page;
    private int ID_User;





    private User user;




    private List<Post> posts;


    public Page(
        String Name,        String Description,        int ID_Page,        int ID_User    ) {
        this.Name = Name;
        this.Description = Description;
        this.ID_Page = ID_Page;
        this.ID_User = ID_User;
        this.posts = new ArrayList<>();
    }

    public Page(
        String Name,        String Description,        int ID_Page,        int ID_User        ArrayList<Post> posts    ) {
        this.Name = Name;
        this.Description = Description;
        this.ID_Page = ID_Page;
        this.ID_User = ID_User;
        this.posts = posts;
    }

    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getDescription() {
        return Description;
    }

    public void setDescription(String Description) {
        this.Description = Description;
    }
    public int getId_page() {
        return ID_Page;
    }

    public void setId_page(int ID_Page) {
        this.ID_Page = ID_Page;
    }
    public int getId_user() {
        return ID_User;
    }

    public void setId_user(int ID_User) {
        this.ID_User = ID_User;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }
    public List<Post> getPosts() {
        return posts;
    }

    public void addPost(Post post) {
        this.posts.add(post);
    }

}