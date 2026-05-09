





import java.util.List;
import java.util.ArrayList;

public class highlevelnets_hlpn_ArcTP extends Arc {






    private Place place;




    private Transition transition;




    private TokenVariadicExpression tokenvariadicexpression;


    public highlevelnets_hlpn_ArcTP(
    ) {
        super(
        );
    }



    public Place getPlace() {
        return place;
    }

    public void setPlace(Place place) {
        this.place = place;
    }
    public Transition getTransition() {
        return transition;
    }

    public void setTransition(Transition transition) {
        this.transition = transition;
    }
    public TokenVariadicExpression getTokenvariadicexpression() {
        return tokenvariadicexpression;
    }

    public void setTokenvariadicexpression(TokenVariadicExpression tokenvariadicexpression) {
        this.tokenvariadicexpression = tokenvariadicexpression;
    }

}