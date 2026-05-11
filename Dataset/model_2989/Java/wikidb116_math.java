





import java.util.List;
import java.util.ArrayList;

public class wikidb116_math  {

    private int math_html_conservativeness;
    private String math_outputhash;
    private String math_inputhash;
    private String math_mathml;
    private String math_html;



    public wikidb116_math(
        int math_html_conservativeness,        String math_outputhash,        String math_inputhash,        String math_mathml,        String math_html    ) {
        this.math_html_conservativeness = math_html_conservativeness;
        this.math_outputhash = math_outputhash;
        this.math_inputhash = math_inputhash;
        this.math_mathml = math_mathml;
        this.math_html = math_html;
    }


    public int getMath_html_conservativeness() {
        return math_html_conservativeness;
    }

    public void setMath_html_conservativeness(int math_html_conservativeness) {
        this.math_html_conservativeness = math_html_conservativeness;
    }
    public String getMath_outputhash() {
        return math_outputhash;
    }

    public void setMath_outputhash(String math_outputhash) {
        this.math_outputhash = math_outputhash;
    }
    public String getMath_inputhash() {
        return math_inputhash;
    }

    public void setMath_inputhash(String math_inputhash) {
        this.math_inputhash = math_inputhash;
    }
    public String getMath_mathml() {
        return math_mathml;
    }

    public void setMath_mathml(String math_mathml) {
        this.math_mathml = math_mathml;
    }
    public String getMath_html() {
        return math_html;
    }

    public void setMath_html(String math_html) {
        this.math_html = math_html;
    }


}