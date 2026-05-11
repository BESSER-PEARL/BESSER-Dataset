





import java.util.List;
import java.util.ArrayList;

public class party_Tag  {

    private String value;
    private String name;
    private String comment;





    private party_Tagged party_tagged;


    public party_Tag(
        String value,        String name,        String comment    ) {
        this.value = value;
        this.name = name;
        this.comment = comment;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }

    public party_Tagged getParty_tagged() {
        return party_tagged;
    }

    public void setParty_tagged(party_Tagged party_tagged) {
        this.party_tagged = party_tagged;
    }

}