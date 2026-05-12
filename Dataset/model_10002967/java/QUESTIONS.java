





import java.util.List;
import java.util.ArrayList;

public class QUESTIONS  {

    private String statusId;
    private int score;
    private String question;
    private String createdAt;
    private String _id;
    private String userId;
    private String productId;
    private String answer;





    private PRODUCT product;




    private USER user;


    public QUESTIONS(
        String statusId,        int score,        String question,        String createdAt,        String _id,        String userId,        String productId,        String answer    ) {
        this.statusId = statusId;
        this.score = score;
        this.question = question;
        this.createdAt = createdAt;
        this._id = _id;
        this.userId = userId;
        this.productId = productId;
        this.answer = answer;
    }


    public String getStatusid() {
        return statusId;
    }

    public void setStatusid(String statusId) {
        this.statusId = statusId;
    }
    public int getScore() {
        return score;
    }

    public void setScore(int score) {
        this.score = score;
    }
    public String getQuestion() {
        return question;
    }

    public void setQuestion(String question) {
        this.question = question;
    }
    public String getCreatedat() {
        return createdAt;
    }

    public void setCreatedat(String createdAt) {
        this.createdAt = createdAt;
    }
    public String get_id() {
        return _id;
    }

    public void set_id(String _id) {
        this._id = _id;
    }
    public String getUserid() {
        return userId;
    }

    public void setUserid(String userId) {
        this.userId = userId;
    }
    public String getProductid() {
        return productId;
    }

    public void setProductid(String productId) {
        this.productId = productId;
    }
    public String getAnswer() {
        return answer;
    }

    public void setAnswer(String answer) {
        this.answer = answer;
    }

    public PRODUCT getProduct() {
        return product;
    }

    public void setProduct(PRODUCT product) {
        this.product = product;
    }
    public USER getUser() {
        return user;
    }

    public void setUser(USER user) {
        this.user = user;
    }

}