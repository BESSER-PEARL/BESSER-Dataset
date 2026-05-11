





import java.util.List;
import java.util.ArrayList;

public class data_Transformation extends Attachment {






    private data_Content data_content;




    private List<data_Content> data_contents;


    public data_Transformation(
    ) {
        super(
        );
        this.data_contents = new ArrayList<>();
    }

    public data_Transformation(
        ArrayList<data_Content> data_contents    ) {
        this.data_contents = data_contents;
    }


    public data_Content getData_content() {
        return data_content;
    }

    public void setData_content(data_Content data_content) {
        this.data_content = data_content;
    }
    public List<data_Content> getData_contents() {
        return data_contents;
    }

    public void addData_content(Data_content data_content) {
        this.data_contents.add(data_content);
    }

}