




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Account  {

    private String Name;
    private LocalDate created;
    private boolean isClosed;
    private LocalDate closed;





    private AddPost addpost;




    private User user;


    public Account(
        String Name,        LocalDate created,        boolean isClosed,        LocalDate closed    ) {
        this.Name = Name;
        this.created = created;
        this.isClosed = isClosed;
        this.closed = closed;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public LocalDate getCreated() {
        return created;
    }

    public void setCreated(LocalDate created) {
        this.created = created;
    }
    public boolean getIsclosed() {
        return isClosed;
    }

    public void setIsclosed(boolean isClosed) {
        this.isClosed = isClosed;
    }
    public LocalDate getClosed() {
        return closed;
    }

    public void setClosed(LocalDate closed) {
        this.closed = closed;
    }

    public AddPost getAddpost() {
        return addpost;
    }

    public void setAddpost(AddPost addpost) {
        this.addpost = addpost;
    }
    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}