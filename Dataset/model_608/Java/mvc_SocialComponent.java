





import java.util.List;
import java.util.ArrayList;

public class mvc_SocialComponent extends View {

    private String socialname;
    private String social;



    public mvc_SocialComponent(
        String socialname,        String social    ) {
        super(
        );
        this.socialname = socialname;
        this.social = social;
    }


    public String getSocialname() {
        return socialname;
    }

    public void setSocialname(String socialname) {
        this.socialname = socialname;
    }
    public String getSocial() {
        return social;
    }

    public void setSocial(String social) {
        this.social = social;
    }


}