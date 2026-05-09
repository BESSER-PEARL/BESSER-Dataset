





import java.util.List;
import java.util.ArrayList;

public class highlevelnets_hlpn_ArcTP extends Arc {

    private int secondTimeConstraint;
    private int firstTimeConstraint;





    private Place place;




    private TokenVariadicExpression tokenvariadicexpression;


    public highlevelnets_hlpn_ArcTP(
        int secondTimeConstraint,        int firstTimeConstraint    ) {
        super(
        );
        this.secondTimeConstraint = secondTimeConstraint;
        this.firstTimeConstraint = firstTimeConstraint;
    }


    public int getSecondtimeconstraint() {
        return secondTimeConstraint;
    }

    public void setSecondtimeconstraint(int secondTimeConstraint) {
        this.secondTimeConstraint = secondTimeConstraint;
    }
    public int getFirsttimeconstraint() {
        return firstTimeConstraint;
    }

    public void setFirsttimeconstraint(int firstTimeConstraint) {
        this.firstTimeConstraint = firstTimeConstraint;
    }

    public Place getPlace() {
        return place;
    }

    public void setPlace(Place place) {
        this.place = place;
    }
    public TokenVariadicExpression getTokenvariadicexpression() {
        return tokenvariadicexpression;
    }

    public void setTokenvariadicexpression(TokenVariadicExpression tokenvariadicexpression) {
        this.tokenvariadicexpression = tokenvariadicexpression;
    }

}