





import java.util.List;
import java.util.ArrayList;

public class data_InformationObject extends Item {

    private String name;





    private data_StarRanking data_starranking;




    private List<data_ViewRanking> data_viewrankings;




    private data_ThumbRanking data_thumbranking;




    private List<data_StarRanking> data_starrankings;




    private List<data_Image> data_images;




    private List<data_Binary> data_binarys;




    private data_ViewRanking data_viewranking;




    private List<data_ThumbRanking> data_thumbrankings;


    public data_InformationObject(
        String name    ) {
        super(
        );
        this.name = name;
        this.data_viewrankings = new ArrayList<>();
        this.data_starrankings = new ArrayList<>();
        this.data_images = new ArrayList<>();
        this.data_binarys = new ArrayList<>();
        this.data_thumbrankings = new ArrayList<>();
    }

    public data_InformationObject(
        String name        ArrayList<data_ViewRanking> data_viewrankings,        ArrayList<data_StarRanking> data_starrankings,        ArrayList<data_Image> data_images,        ArrayList<data_Binary> data_binarys,        ArrayList<data_ThumbRanking> data_thumbrankings    ) {
        this.name = name;
        this.data_viewrankings = data_viewrankings;
        this.data_starrankings = data_starrankings;
        this.data_images = data_images;
        this.data_binarys = data_binarys;
        this.data_thumbrankings = data_thumbrankings;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public data_StarRanking getData_starranking() {
        return data_starranking;
    }

    public void setData_starranking(data_StarRanking data_starranking) {
        this.data_starranking = data_starranking;
    }
    public List<data_ViewRanking> getData_viewrankings() {
        return data_viewrankings;
    }

    public void addData_viewranking(Data_viewranking data_viewranking) {
        this.data_viewrankings.add(data_viewranking);
    }
    public data_ThumbRanking getData_thumbranking() {
        return data_thumbranking;
    }

    public void setData_thumbranking(data_ThumbRanking data_thumbranking) {
        this.data_thumbranking = data_thumbranking;
    }
    public List<data_StarRanking> getData_starrankings() {
        return data_starrankings;
    }

    public void addData_starranking(Data_starranking data_starranking) {
        this.data_starrankings.add(data_starranking);
    }
    public List<data_Image> getData_images() {
        return data_images;
    }

    public void addData_image(Data_image data_image) {
        this.data_images.add(data_image);
    }
    public List<data_Binary> getData_binarys() {
        return data_binarys;
    }

    public void addData_binary(Data_binary data_binary) {
        this.data_binarys.add(data_binary);
    }
    public data_ViewRanking getData_viewranking() {
        return data_viewranking;
    }

    public void setData_viewranking(data_ViewRanking data_viewranking) {
        this.data_viewranking = data_viewranking;
    }
    public List<data_ThumbRanking> getData_thumbrankings() {
        return data_thumbrankings;
    }

    public void addData_thumbranking(Data_thumbranking data_thumbranking) {
        this.data_thumbrankings.add(data_thumbranking);
    }

}