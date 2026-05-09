





import java.util.List;
import java.util.ArrayList;

public class reviews_Repository  {

    private String description;
    private String taskRepositoryUrl;
    private String taskConnectorKind;
    private String taskRepository;





    private reviews_User reviews_user;




    private List<reviews_User> reviews_users;




    private reviews_Review reviews_review;




    private List<reviews_Review> reviews_reviews;


    public reviews_Repository(
        String description,        String taskRepositoryUrl,        String taskConnectorKind,        String taskRepository    ) {
        this.description = description;
        this.taskRepositoryUrl = taskRepositoryUrl;
        this.taskConnectorKind = taskConnectorKind;
        this.taskRepository = taskRepository;
        this.reviews_users = new ArrayList<>();
        this.reviews_reviews = new ArrayList<>();
    }

    public reviews_Repository(
        String description,        String taskRepositoryUrl,        String taskConnectorKind,        String taskRepository        ArrayList<reviews_User> reviews_users,        ArrayList<reviews_Review> reviews_reviews    ) {
        this.description = description;
        this.taskRepositoryUrl = taskRepositoryUrl;
        this.taskConnectorKind = taskConnectorKind;
        this.taskRepository = taskRepository;
        this.reviews_users = reviews_users;
        this.reviews_reviews = reviews_reviews;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getTaskrepositoryurl() {
        return taskRepositoryUrl;
    }

    public void setTaskrepositoryurl(String taskRepositoryUrl) {
        this.taskRepositoryUrl = taskRepositoryUrl;
    }
    public String getTaskconnectorkind() {
        return taskConnectorKind;
    }

    public void setTaskconnectorkind(String taskConnectorKind) {
        this.taskConnectorKind = taskConnectorKind;
    }
    public String getTaskrepository() {
        return taskRepository;
    }

    public void setTaskrepository(String taskRepository) {
        this.taskRepository = taskRepository;
    }

    public reviews_User getReviews_user() {
        return reviews_user;
    }

    public void setReviews_user(reviews_User reviews_user) {
        this.reviews_user = reviews_user;
    }
    public List<reviews_User> getReviews_users() {
        return reviews_users;
    }

    public void addReviews_user(Reviews_user reviews_user) {
        this.reviews_users.add(reviews_user);
    }
    public reviews_Review getReviews_review() {
        return reviews_review;
    }

    public void setReviews_review(reviews_Review reviews_review) {
        this.reviews_review = reviews_review;
    }
    public List<reviews_Review> getReviews_reviews() {
        return reviews_reviews;
    }

    public void addReviews_review(Reviews_review reviews_review) {
        this.reviews_reviews.add(reviews_review);
    }

}