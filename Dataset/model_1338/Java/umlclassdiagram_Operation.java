





import java.util.List;
import java.util.ArrayList;

public class umlclassdiagram_Operation extends Feature {






    private List<umlclassdiagram_Parameter> umlclassdiagram_parameters;


    public umlclassdiagram_Operation(
    ) {
        super(
        );
        this.umlclassdiagram_parameters = new ArrayList<>();
    }

    public umlclassdiagram_Operation(
        ArrayList<umlclassdiagram_Parameter> umlclassdiagram_parameters    ) {
        this.umlclassdiagram_parameters = umlclassdiagram_parameters;
    }


    public List<umlclassdiagram_Parameter> getUmlclassdiagram_parameters() {
        return umlclassdiagram_parameters;
    }

    public void addUmlclassdiagram_parameter(Umlclassdiagram_parameter umlclassdiagram_parameter) {
        this.umlclassdiagram_parameters.add(umlclassdiagram_parameter);
    }

}