





import java.util.List;
import java.util.ArrayList;

public class model_ExtraBall extends Ball {

    private String isValidBall;
    private String extraType;



    public model_ExtraBall(
        String isValidBall,        String extraType    ) {
        super(
        );
        this.isValidBall = isValidBall;
        this.extraType = extraType;
    }


    public String getIsvalidball() {
        return isValidBall;
    }

    public void setIsvalidball(String isValidBall) {
        this.isValidBall = isValidBall;
    }
    public String getExtratype() {
        return extraType;
    }

    public void setExtratype(String extraType) {
        this.extraType = extraType;
    }


}