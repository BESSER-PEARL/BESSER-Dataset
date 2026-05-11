





import java.util.List;
import java.util.ArrayList;

public class df_Tag  {

    private String identifiers;





    private df_Action df_action;


    public df_Tag(
        String identifiers    ) {
        this.identifiers = identifiers;
    }


    public String getIdentifiers() {
        return identifiers;
    }

    public void setIdentifiers(String identifiers) {
        this.identifiers = identifiers;
    }

    public df_Action getDf_action() {
        return df_action;
    }

    public void setDf_action(df_Action df_action) {
        this.df_action = df_action;
    }

}