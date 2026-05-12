





import java.util.List;
import java.util.ArrayList;

public class schema_ActionLike  {

    private String pluralPastTense;
    private String imperativeTense;
    private String pastTense;
    private String tenses;
    private String pluralPresentTense;
    private String presentTense;



    public schema_ActionLike(
        String pluralPastTense,        String imperativeTense,        String pastTense,        String tenses,        String pluralPresentTense,        String presentTense    ) {
        this.pluralPastTense = pluralPastTense;
        this.imperativeTense = imperativeTense;
        this.pastTense = pastTense;
        this.tenses = tenses;
        this.pluralPresentTense = pluralPresentTense;
        this.presentTense = presentTense;
    }


    public String getPluralpasttense() {
        return pluralPastTense;
    }

    public void setPluralpasttense(String pluralPastTense) {
        this.pluralPastTense = pluralPastTense;
    }
    public String getImperativetense() {
        return imperativeTense;
    }

    public void setImperativetense(String imperativeTense) {
        this.imperativeTense = imperativeTense;
    }
    public String getPasttense() {
        return pastTense;
    }

    public void setPasttense(String pastTense) {
        this.pastTense = pastTense;
    }
    public String getTenses() {
        return tenses;
    }

    public void setTenses(String tenses) {
        this.tenses = tenses;
    }
    public String getPluralpresenttense() {
        return pluralPresentTense;
    }

    public void setPluralpresenttense(String pluralPresentTense) {
        this.pluralPresentTense = pluralPresentTense;
    }
    public String getPresenttense() {
        return presentTense;
    }

    public void setPresenttense(String presentTense) {
        this.presentTense = presentTense;
    }


}