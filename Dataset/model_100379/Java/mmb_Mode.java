





import java.util.List;
import java.util.ArrayList;

public class mmb_Mode  {

    private String Shape;
    private float Dimension;
    private String Name;
    private boolean InitialState;





    private mmb_Automaton mmb_automaton;


    public mmb_Mode(
        String Shape,        float Dimension,        String Name,        boolean InitialState    ) {
        this.Shape = Shape;
        this.Dimension = Dimension;
        this.Name = Name;
        this.InitialState = InitialState;
    }


    public String getShape() {
        return Shape;
    }

    public void setShape(String Shape) {
        this.Shape = Shape;
    }
    public float getDimension() {
        return Dimension;
    }

    public void setDimension(float Dimension) {
        this.Dimension = Dimension;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public boolean getInitialstate() {
        return InitialState;
    }

    public void setInitialstate(boolean InitialState) {
        this.InitialState = InitialState;
    }

    public mmb_Automaton getMmb_automaton() {
        return mmb_automaton;
    }

    public void setMmb_automaton(mmb_Automaton mmb_automaton) {
        this.mmb_automaton = mmb_automaton;
    }

}