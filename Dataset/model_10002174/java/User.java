





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String nickname;
    private String bio;
    private int level;
    private String avatar;
    private String links;
    private String email;



    public User(
        String nickname,        String bio,        int level,        String avatar,        String links,        String email    ) {
        this.nickname = nickname;
        this.bio = bio;
        this.level = level;
        this.avatar = avatar;
        this.links = links;
        this.email = email;
    }


    public String getNickname() {
        return nickname;
    }

    public void setNickname(String nickname) {
        this.nickname = nickname;
    }
    public String getBio() {
        return bio;
    }

    public void setBio(String bio) {
        this.bio = bio;
    }
    public int getLevel() {
        return level;
    }

    public void setLevel(int level) {
        this.level = level;
    }
    public String getAvatar() {
        return avatar;
    }

    public void setAvatar(String avatar) {
        this.avatar = avatar;
    }
    public String getLinks() {
        return links;
    }

    public void setLinks(String links) {
        this.links = links;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }


}