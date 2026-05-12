





import java.util.List;
import java.util.ArrayList;

public class ExerciseMachine  {

    private int size;
    private int id;
    private String name;
    private String type;





    private Product product;


    public ExerciseMachine(
        int size,        int id,        String name,        String type    ) {
        this.size = size;
        this.id = id;
        this.name = name;
        this.type = type;
    }


    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
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

    public Product getProduct() {
        return product;
    }

    public void setProduct(Product product) {
        this.product = product;
    }

}