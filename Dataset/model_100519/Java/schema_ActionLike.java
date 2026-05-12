





import java.util.List;
import java.util.ArrayList;

public class schema_ActionLike  {

    private String pluralPastTense;
    private String tenses;
    private String pastTense;
    private String pluralPresentTense;
    private String presentTense;
    private String imperativeTense;



    public schema_ActionLike(
        String pluralPastTense,        String tenses,        String pastTense,        String pluralPresentTense,        String presentTense,        String imperativeTense    ) {
        this.pluralPastTense = pluralPastTense;
        this.tenses = tenses;
        this.pastTense = pastTense;
        this.pluralPresentTense = pluralPresentTense;
        this.presentTense = presentTense;
        this.imperativeTense = imperativeTense;
    }


    public String getPluralpasttense() {
        return pluralPastTense;
    }

    public void setPluralpasttense(String pluralPastTense) {
        this.pluralPastTense = pluralPastTense;
    }
    public String getTenses() {
        return tenses;
    }

    public void setTenses(String tenses) {
        this.tenses = tenses;
    }
    public String getPasttense() {
        return pastTense;
    }

    public void setPasttense(String pastTense) {
        this.pastTense = pastTense;
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
    public String getImperativetense() {
        return imperativeTense;
    }

    public void setImperativetense(String imperativeTense) {
        this.imperativeTense = imperativeTense;
    }


}