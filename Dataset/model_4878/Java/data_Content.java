





import java.util.List;
import java.util.ArrayList;

public class data_Content extends InformationObject {

    private String locale;





    private List<data_Transformation> data_transformations;




    private data_Content data_content;




    private List<data_Video> data_videos;




    private List<data_Document> data_documents;




    private List<data_Content> data_contents;




    private data_Transformation data_transformation;


    public data_Content(
        String locale    ) {
        super(
        );
        this.locale = locale;
        this.data_transformations = new ArrayList<>();
        this.data_videos = new ArrayList<>();
        this.data_documents = new ArrayList<>();
        this.data_contents = new ArrayList<>();
    }

    public data_Content(
        String locale        ArrayList<data_Transformation> data_transformations,        ArrayList<data_Video> data_videos,        ArrayList<data_Document> data_documents,        ArrayList<data_Content> data_contents    ) {
        this.locale = locale;
        this.data_transformations = data_transformations;
        this.data_videos = data_videos;
        this.data_documents = data_documents;
        this.data_contents = data_contents;
    }

    public String getLocale() {
        return locale;
    }

    public void setLocale(String locale) {
        this.locale = locale;
    }

    public List<data_Transformation> getData_transformations() {
        return data_transformations;
    }

    public void addData_transformation(Data_transformation data_transformation) {
        this.data_transformations.add(data_transformation);
    }
    public data_Content getData_content() {
        return data_content;
    }

    public void setData_content(data_Content data_content) {
        this.data_content = data_content;
    }
    public List<data_Video> getData_videos() {
        return data_videos;
    }

    public void addData_video(Data_video data_video) {
        this.data_videos.add(data_video);
    }
    public List<data_Document> getData_documents() {
        return data_documents;
    }

    public void addData_document(Data_document data_document) {
        this.data_documents.add(data_document);
    }
    public List<data_Content> getData_contents() {
        return data_contents;
    }

    public void addData_content(Data_content data_content) {
        this.data_contents.add(data_content);
    }
    public data_Transformation getData_transformation() {
        return data_transformation;
    }

    public void setData_transformation(data_Transformation data_transformation) {
        this.data_transformation = data_transformation;
    }

}