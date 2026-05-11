





import java.util.List;
import java.util.ArrayList;

public class Data_Method  {

    private String return_;
    private String name;
    private String encapsulation;





    private Data_Class data_class;


    public Data_Method(
        String return_,        String name,        String encapsulation    ) {
        this.return_ = return_;
        this.name = name;
        this.encapsulation = encapsulation;
    }


    public String getReturn_() {
        return return_;
    }

    public void setReturn_(String return_) {
        this.return_ = return_;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getEncapsulation() {
        return encapsulation;
    }

    public void setEncapsulation(String encapsulation) {
        this.encapsulation = encapsulation;
    }

    public Data_Class getData_class() {
        return data_class;
    }

    public void setData_class(Data_Class data_class) {
        this.data_class = data_class;
    }

}