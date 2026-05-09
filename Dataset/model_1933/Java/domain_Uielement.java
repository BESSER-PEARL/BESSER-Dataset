





import java.util.List;
import java.util.ArrayList;

public class domain_Uielement extends Orderable, StyleElement, MenuHolder, NickNamed, EnabledUIItem, Categorized, FlexFields {

    private String uid;





    private domain_Column domain_column;


    public domain_Uielement(
        String uid    ) {
        super(
        );
        this.uid = uid;
    }


    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }

    public domain_Column getDomain_column() {
        return domain_column;
    }

    public void setDomain_column(domain_Column domain_column) {
        this.domain_column = domain_column;
    }

}