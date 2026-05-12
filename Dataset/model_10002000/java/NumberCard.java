





import java.util.List;
import java.util.ArrayList;

public class NumberCard  {

    private String NumberCard_Color__String_;
    private String attribute2;
    private String attribute;
    private String NumberCard__;



    public NumberCard(
        String NumberCard_Color__String_,        String attribute2,        String attribute,        String NumberCard__    ) {
        this.NumberCard_Color__String_ = NumberCard_Color__String_;
        this.attribute2 = attribute2;
        this.attribute = attribute;
        this.NumberCard__ = NumberCard__;
    }


    public String getNumbercard_color__string_() {
        return NumberCard_Color__String_;
    }

    public void setNumbercard_color__string_(String NumberCard_Color__String_) {
        this.NumberCard_Color__String_ = NumberCard_Color__String_;
    }
    public String getAttribute2() {
        return attribute2;
    }

    public void setAttribute2(String attribute2) {
        this.attribute2 = attribute2;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public String getNumbercard__() {
        return NumberCard__;
    }

    public void setNumbercard__(String NumberCard__) {
        this.NumberCard__ = NumberCard__;
    }


}