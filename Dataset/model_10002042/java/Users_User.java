





import java.util.List;
import java.util.ArrayList;

public class Users_User  {

    private String username;
    private String groups;
    private int UserID;
    private String password;
    private String email;
    private String Privacy;
    private String FriendRequests;
    private String Full_Name;
    private None Friends;
    private int Age;
    private String Gender;
    private String pages;
    private String Messages;



    public Users_User(
        String username,        String groups,        int UserID,        String password,        String email,        String Privacy,        String FriendRequests,        String Full_Name,        None Friends,        int Age,        String Gender,        String pages,        String Messages    ) {
        this.username = username;
        this.groups = groups;
        this.UserID = UserID;
        this.password = password;
        this.email = email;
        this.Privacy = Privacy;
        this.FriendRequests = FriendRequests;
        this.Full_Name = Full_Name;
        this.Friends = Friends;
        this.Age = Age;
        this.Gender = Gender;
        this.pages = pages;
        this.Messages = Messages;
    }


    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getGroups() {
        return groups;
    }

    public void setGroups(String groups) {
        this.groups = groups;
    }
    public int getUserid() {
        return UserID;
    }

    public void setUserid(int UserID) {
        this.UserID = UserID;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getPrivacy() {
        return Privacy;
    }

    public void setPrivacy(String Privacy) {
        this.Privacy = Privacy;
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
    public None getFriends() {
        return Friends;
    }

    public void setFriends(None Friends) {
        this.Friends = Friends;
    }
    public int getAge() {
        return Age;
    }

    public void setAge(int Age) {
        this.Age = Age;
    }
    public String getGender() {
        return Gender;
    }

    public void setGender(String Gender) {
        this.Gender = Gender;
    }
    public String getPages() {
        return pages;
    }

    public void setPages(String pages) {
        this.pages = pages;
    }
    public String getMessages() {
        return Messages;
    }

    public void setMessages(String Messages) {
        this.Messages = Messages;
    }


}