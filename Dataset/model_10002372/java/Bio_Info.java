





import java.util.List;
import java.util.ArrayList;

public class Bio_Info  {

    private String age;
    private int average_ratings;
    private String favourite_cuisine;
    private String name;





    private User user;


    public Bio_Info(
        String age,        int average_ratings,        String favourite_cuisine,        String name    ) {
        this.age = age;
        this.average_ratings = average_ratings;
        this.favourite_cuisine = favourite_cuisine;
        this.name = name;
    }


    public String getAge() {
        return age;
    }

    public void setAge(String age) {
        this.age = age;
    }
    public int getAverage_ratings() {
        return average_ratings;
    }

    public void setAverage_ratings(int average_ratings) {
        this.average_ratings = average_ratings;
    }
    public String getFavourite_cuisine() {
        return favourite_cuisine;
    }

    public void setFavourite_cuisine(String favourite_cuisine) {
        this.favourite_cuisine = favourite_cuisine;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}