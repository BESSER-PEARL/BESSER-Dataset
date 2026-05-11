





import java.util.List;
import java.util.ArrayList;

public class model_Primitive  {

    private String name;





    private model_FigureContainer model_figurecontainer;




    private model_Connection model_connection;




    private model_Connection model_connection;




    private model_Symbol model_symbol;


    public model_Primitive(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public model_FigureContainer getModel_figurecontainer() {
        return model_figurecontainer;
    }

    public void setModel_figurecontainer(model_FigureContainer model_figurecontainer) {
        this.model_figurecontainer = model_figurecontainer;
    }
    public model_Connection getModel_connection() {
        return model_connection;
    }

    public void setModel_connection(model_Connection model_connection) {
        this.model_connection = model_connection;
    }
    public model_Connection getModel_connection() {
        return model_connection;
    }

    public void setModel_connection(model_Connection model_connection) {
        this.model_connection = model_connection;
    }
    public model_Symbol getModel_symbol() {
        return model_symbol;
    }

    public void setModel_symbol(model_Symbol model_symbol) {
        this.model_symbol = model_symbol;
    }

}