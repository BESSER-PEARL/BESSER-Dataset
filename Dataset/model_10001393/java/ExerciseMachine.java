





import java.util.List;
import java.util.ArrayList;

public class ExerciseMachine  {

    private String name;
    private int id;
    private int size;
    private String type;





    private Product product;


    public ExerciseMachine(
        String name,        int id,        int size,        String type    ) {
        this.name = name;
        this.id = id;
        this.size = size;
        this.type = type;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
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