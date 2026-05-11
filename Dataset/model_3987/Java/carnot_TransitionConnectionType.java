





import java.util.List;
import java.util.ArrayList;

public class carnot_TransitionConnectionType extends IConnectionSymbol {

    private String points;





    private carnot_TransitionType carnot_transitiontype;




    private carnot_ISymbolContainer carnot_isymbolcontainer;




    private carnot_TransitionType carnot_transitiontype;


    public carnot_TransitionConnectionType(
        String points    ) {
        super(
        );
        this.points = points;
    }


    public String getPoints() {
        return points;
    }

    public void setPoints(String points) {
        this.points = points;
    }

    public carnot_TransitionType getCarnot_transitiontype() {
        return carnot_transitiontype;
    }

    public void setCarnot_transitiontype(carnot_TransitionType carnot_transitiontype) {
        this.carnot_transitiontype = carnot_transitiontype;
    }
    public carnot_ISymbolContainer getCarnot_isymbolcontainer() {
        return carnot_isymbolcontainer;
    }

    public void setCarnot_isymbolcontainer(carnot_ISymbolContainer carnot_isymbolcontainer) {
        this.carnot_isymbolcontainer = carnot_isymbolcontainer;
    }
    public carnot_TransitionType getCarnot_transitiontype() {
        return carnot_transitiontype;
    }

    public void setCarnot_transitiontype(carnot_TransitionType carnot_transitiontype) {
        this.carnot_transitiontype = carnot_transitiontype;
    }

}