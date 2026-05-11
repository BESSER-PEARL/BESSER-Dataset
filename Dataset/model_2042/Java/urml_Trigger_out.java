





import java.util.List;
import java.util.ArrayList;

public class urml_Trigger_out  {






    private List<urml_Expression> urml_expressions;




    private urml_Signal urml_signal;




    private urml_Port urml_port;


    public urml_Trigger_out(
    ) {
        this.urml_expressions = new ArrayList<>();
    }

    public urml_Trigger_out(
        ArrayList<urml_Expression> urml_expressions    ) {
        this.urml_expressions = urml_expressions;
    }


    public List<urml_Expression> getUrml_expressions() {
        return urml_expressions;
    }

    public void addUrml_expression(Urml_expression urml_expression) {
        this.urml_expressions.add(urml_expression);
    }
    public urml_Signal getUrml_signal() {
        return urml_signal;
    }

    public void setUrml_signal(urml_Signal urml_signal) {
        this.urml_signal = urml_signal;
    }
    public urml_Port getUrml_port() {
        return urml_port;
    }

    public void setUrml_port(urml_Port urml_port) {
        this.urml_port = urml_port;
    }

}