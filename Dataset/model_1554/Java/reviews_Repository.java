





import java.util.List;
import java.util.ArrayList;

public class reviews_Repository  {

    private String description;
    private String taskRepositoryUrl;
    private String taskRepository;
    private String taskConnectorKind;





    private List<reviews_Review> reviews_reviews;




    private reviews_Review reviews_review;


    public reviews_Repository(
        String description,        String taskRepositoryUrl,        String taskRepository,        String taskConnectorKind    ) {
        this.description = description;
        this.taskRepositoryUrl = taskRepositoryUrl;
        this.taskRepository = taskRepository;
        this.taskConnectorKind = taskConnectorKind;
        this.reviews_reviews = new ArrayList<>();
    }

    public reviews_Repository(
        String description,        String taskRepositoryUrl,        String taskRepository,        String taskConnectorKind        ArrayList<reviews_Review> reviews_reviews    ) {
        this.description = description;
        this.taskRepositoryUrl = taskRepositoryUrl;
        this.taskRepository = taskRepository;
        this.taskConnectorKind = taskConnectorKind;
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
    public String getTaskrepository() {
        return taskRepository;
    }

    public void setTaskrepository(String taskRepository) {
        this.taskRepository = taskRepository;
    }
    public String getTaskconnectorkind() {
        return taskConnectorKind;
    }

    public void setTaskconnectorkind(String taskConnectorKind) {
        this.taskConnectorKind = taskConnectorKind;
    }

    public List<reviews_Review> getReviews_reviews() {
        return reviews_reviews;
    }

    public void addReviews_review(Reviews_review reviews_review) {
        this.reviews_reviews.add(reviews_review);
    }
    public reviews_Review getReviews_review() {
        return reviews_review;
    }

    public void setReviews_review(reviews_Review reviews_review) {
        this.reviews_review = reviews_review;
    }

}