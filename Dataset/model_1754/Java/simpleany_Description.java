





import java.util.List;
import java.util.ArrayList;

public class simpleany_Description  {

    private String mixed;
    private String keyword;





    private simpleany_BookType simpleany_booktype;




    private simpleany_Description simpleany_description;


    public simpleany_Description(
        String mixed,        String keyword    ) {
        this.mixed = mixed;
        this.keyword = keyword;
    }


    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getKeyword() {
        return keyword;
    }

    public void setKeyword(String keyword) {
        this.keyword = keyword;
    }

    public simpleany_BookType getSimpleany_booktype() {
        return simpleany_booktype;
    }

    public void setSimpleany_booktype(simpleany_BookType simpleany_booktype) {
        this.simpleany_booktype = simpleany_booktype;
    }
    public simpleany_Description getSimpleany_description() {
        return simpleany_description;
    }

    public void setSimpleany_description(simpleany_Description simpleany_description) {
        this.simpleany_description = simpleany_description;
    }

}