





import java.util.List;
import java.util.ArrayList;

public class model_R4EUserReviews  {

    private String createdReviews;
    private String name;





    private model_R4EReviewGroup model_r4ereviewgroup;




    private List<model_MapNameToReview> model_mapnametoreviews;




    private model_MapUserIDToUserReviews model_mapuseridtouserreviews;


    public model_R4EUserReviews(
        String createdReviews,        String name    ) {
        this.createdReviews = createdReviews;
        this.name = name;
        this.model_mapnametoreviews = new ArrayList<>();
    }

    public model_R4EUserReviews(
        String createdReviews,        String name        ArrayList<model_MapNameToReview> model_mapnametoreviews    ) {
        this.createdReviews = createdReviews;
        this.name = name;
        this.model_mapnametoreviews = model_mapnametoreviews;
    }

    public String getCreatedreviews() {
        return createdReviews;
    }

    public void setCreatedreviews(String createdReviews) {
        this.createdReviews = createdReviews;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public model_R4EReviewGroup getModel_r4ereviewgroup() {
        return model_r4ereviewgroup;
    }

    public void setModel_r4ereviewgroup(model_R4EReviewGroup model_r4ereviewgroup) {
        this.model_r4ereviewgroup = model_r4ereviewgroup;
    }
    public List<model_MapNameToReview> getModel_mapnametoreviews() {
        return model_mapnametoreviews;
    }

    public void addModel_mapnametoreview(Model_mapnametoreview model_mapnametoreview) {
        this.model_mapnametoreviews.add(model_mapnametoreview);
    }
    public model_MapUserIDToUserReviews getModel_mapuseridtouserreviews() {
        return model_mapuseridtouserreviews;
    }

    public void setModel_mapuseridtouserreviews(model_MapUserIDToUserReviews model_mapuseridtouserreviews) {
        this.model_mapuseridtouserreviews = model_mapuseridtouserreviews;
    }

}