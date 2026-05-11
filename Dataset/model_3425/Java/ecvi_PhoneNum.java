





import java.util.List;
import java.util.ArrayList;

public class ecvi_PhoneNum  {

    private String comment;
    private String number;
    private String type;





    private ecvi_Person ecvi_person;


    public ecvi_PhoneNum(
        String comment,        String number,        String type    ) {
        this.comment = comment;
        this.number = number;
        this.type = type;
    }


    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public ecvi_Person getEcvi_person() {
        return ecvi_person;
    }

    public void setEcvi_person(ecvi_Person ecvi_person) {
        this.ecvi_person = ecvi_person;
    }

}