




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Post  {

    private None status;
    private int ID;
    private LocalDate Created;
    private String Category;
    private String User;
    private float tags;





    private Account account;


    public Post(
        None status,        int ID,        LocalDate Created,        String Category,        String User,        float tags    ) {
        this.status = status;
        this.ID = ID;
        this.Created = Created;
        this.Category = Category;
        this.User = User;
        this.tags = tags;
    }


    public None getStatus() {
        return status;
    }

    public void setStatus(None status) {
        this.status = status;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }
    public LocalDate getCreated() {
        return Created;
    }

    public void setCreated(LocalDate Created) {
        this.Created = Created;
    }
    public String getCategory() {
        return Category;
    }

    public void setCategory(String Category) {
        this.Category = Category;
    }
    public String getUser() {
        return User;
    }

    public void setUser(String User) {
        this.User = User;
    }
    public float getTags() {
        return tags;
    }

    public void setTags(float tags) {
        this.tags = tags;
    }

    public Account getAccount() {
        return account;
    }

    public void setAccount(Account account) {
        this.account = account;
    }

}