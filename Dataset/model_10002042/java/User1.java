





import java.util.List;
import java.util.ArrayList;

public class User1  {

    private String Gender;
    private String password;
    private int UserID;
    private int Age;
    private String Messages;
    private None Friends;
    private String FriendRequests;
    private String Full_Name;
    private String pages;
    private String Privacy;
    private String email;
    private String groups;
    private String username;



    public User1(
        String Gender,        String password,        int UserID,        int Age,        String Messages,        None Friends,        String FriendRequests,        String Full_Name,        String pages,        String Privacy,        String email,        String groups,        String username    ) {
        this.Gender = Gender;
        this.password = password;
        this.UserID = UserID;
        this.Age = Age;
        this.Messages = Messages;
        this.Friends = Friends;
        this.FriendRequests = FriendRequests;
        this.Full_Name = Full_Name;
        this.pages = pages;
        this.Privacy = Privacy;
        this.email = email;
        this.groups = groups;
        this.username = username;
    }


    public String getGender() {
        return Gender;
    }

    public void setGender(String Gender) {
        this.Gender = Gender;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public int getUserid() {
        return UserID;
    }

    public void setUserid(int UserID) {
        this.UserID = UserID;
    }
    public int getAge() {
        return Age;
    }

    public void setAge(int Age) {
        this.Age = Age;
    }
    public String getMessages() {
        return Messages;
    }

    public void setMessages(String Messages) {
        this.Messages = Messages;
    }
    public None getFriends() {
        return Friends;
    }

    public void setFriends(None Friends) {
        this.Friends = Friends;
    }
    public String getFriendrequests() {
        return FriendRequests;
    }

    public void setFriendrequests(String FriendRequests) {
        this.FriendRequests = FriendRequests;
    }
    public String getFull_name() {
        return Full_Name;
    }

    public void setFull_name(String Full_Name) {
        this.Full_Name = Full_Name;
    }
    public String getPages() {
        return pages;
    }

    public void setPages(String pages) {
        this.pages = pages;
    }
    public String getPrivacy() {
        return Privacy;
    }

    public void setPrivacy(String Privacy) {
        this.Privacy = Privacy;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getGroups() {
        return groups;
    }

    public void setGroups(String groups) {
        this.groups = groups;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }


}