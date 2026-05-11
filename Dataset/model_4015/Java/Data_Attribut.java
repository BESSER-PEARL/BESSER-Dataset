





import java.util.List;
import java.util.ArrayList;

public class Data_Attribut  {

    private String name;
    private String type;





    private Data_Classe data_classe;


    public Data_Attribut(
        String name,        String type    ) {
        this.name = name;
        this.type = type;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public Data_Classe getData_classe() {
        return data_classe;
    }

    public void setData_classe(Data_Classe data_classe) {
        this.data_classe = data_classe;
    }

}