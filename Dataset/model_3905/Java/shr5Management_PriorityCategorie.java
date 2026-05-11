





import java.util.List;
import java.util.ArrayList;

public class shr5Management_PriorityCategorie  {

    private String categorieName;
    private int cost;





    private shr5Management_PrioritySystem shr5management_prioritysystem;


    public shr5Management_PriorityCategorie(
        String categorieName,        int cost    ) {
        this.categorieName = categorieName;
        this.cost = cost;
    }


    public String getCategoriename() {
        return categorieName;
    }

    public void setCategoriename(String categorieName) {
        this.categorieName = categorieName;
    }
    public int getCost() {
        return cost;
    }

    public void setCost(int cost) {
        this.cost = cost;
    }

    public shr5Management_PrioritySystem getShr5management_prioritysystem() {
        return shr5management_prioritysystem;
    }

    public void setShr5management_prioritysystem(shr5Management_PrioritySystem shr5management_prioritysystem) {
        this.shr5management_prioritysystem = shr5management_prioritysystem;
    }

}