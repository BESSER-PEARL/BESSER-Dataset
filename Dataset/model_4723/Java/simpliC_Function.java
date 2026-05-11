





import java.util.List;
import java.util.ArrayList;

public class simpliC_Function  {

    private String name;





    private simpliC_Model simplic_model;




    private simpliC_Block simplic_block;




    private simpliC_Call simplic_call;


    public simpliC_Function(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public simpliC_Model getSimplic_model() {
        return simplic_model;
    }

    public void setSimplic_model(simpliC_Model simplic_model) {
        this.simplic_model = simplic_model;
    }
    public simpliC_Block getSimplic_block() {
        return simplic_block;
    }

    public void setSimplic_block(simpliC_Block simplic_block) {
        this.simplic_block = simplic_block;
    }
    public simpliC_Call getSimplic_call() {
        return simplic_call;
    }

    public void setSimplic_call(simpliC_Call simplic_call) {
        this.simplic_call = simplic_call;
    }

}