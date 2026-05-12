





import java.util.List;
import java.util.ArrayList;

public class luniferadoc_richstring_RichStringMailto extends RichStringMarkup {

    private String email;





    private richstring_luniferadoc_XExpression richstring_luniferadoc_xexpression;


    public luniferadoc_richstring_RichStringMailto(
        String email    ) {
        super(
        );
        this.email = email;
    }


    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public richstring_luniferadoc_XExpression getRichstring_luniferadoc_xexpression() {
        return richstring_luniferadoc_xexpression;
    }

    public void setRichstring_luniferadoc_xexpression(richstring_luniferadoc_XExpression richstring_luniferadoc_xexpression) {
        this.richstring_luniferadoc_xexpression = richstring_luniferadoc_xexpression;
    }

}