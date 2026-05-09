





import java.util.List;
import java.util.ArrayList;

public class PagosPim_ParameterList  {






    private PagosPim_Operation pagospim_operation;




    private List<PagosPim_Parameter> pagospim_parameters;


    public PagosPim_ParameterList(
    ) {
        this.pagospim_parameters = new ArrayList<>();
    }

    public PagosPim_ParameterList(
        ArrayList<PagosPim_Parameter> pagospim_parameters    ) {
        this.pagospim_parameters = pagospim_parameters;
    }


    public PagosPim_Operation getPagospim_operation() {
        return pagospim_operation;
    }

    public void setPagospim_operation(PagosPim_Operation pagospim_operation) {
        this.pagospim_operation = pagospim_operation;
    }
    public List<PagosPim_Parameter> getPagospim_parameters() {
        return pagospim_parameters;
    }

    public void addPagospim_parameter(Pagospim_parameter pagospim_parameter) {
        this.pagospim_parameters.add(pagospim_parameter);
    }

}