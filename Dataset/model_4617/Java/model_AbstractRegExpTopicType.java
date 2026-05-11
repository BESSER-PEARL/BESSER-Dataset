





import java.util.List;
import java.util.ArrayList;

public class model_AbstractRegExpTopicType extends TopicType {

    private String regExp;



    public model_AbstractRegExpTopicType(
        String regExp    ) {
        super(
        );
        this.regExp = regExp;
    }


    public String getRegexp() {
        return regExp;
    }

    public void setRegexp(String regExp) {
        this.regExp = regExp;
    }


}