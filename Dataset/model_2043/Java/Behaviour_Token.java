





import java.util.List;
import java.util.ArrayList;

public class Behaviour_Token extends Identifier {






    private List<Behaviour_Colour> behaviour_colours;




    private Behaviour_Description behaviour_description;




    private Behaviour_Place behaviour_place;


    public Behaviour_Token(
    ) {
        super(
        );
        this.behaviour_colours = new ArrayList<>();
    }

    public Behaviour_Token(
        ArrayList<Behaviour_Colour> behaviour_colours    ) {
        this.behaviour_colours = behaviour_colours;
    }


    public List<Behaviour_Colour> getBehaviour_colours() {
        return behaviour_colours;
    }

    public void addBehaviour_colour(Behaviour_colour behaviour_colour) {
        this.behaviour_colours.add(behaviour_colour);
    }
    public Behaviour_Description getBehaviour_description() {
        return behaviour_description;
    }

    public void setBehaviour_description(Behaviour_Description behaviour_description) {
        this.behaviour_description = behaviour_description;
    }
    public Behaviour_Place getBehaviour_place() {
        return behaviour_place;
    }

    public void setBehaviour_place(Behaviour_Place behaviour_place) {
        this.behaviour_place = behaviour_place;
    }

}