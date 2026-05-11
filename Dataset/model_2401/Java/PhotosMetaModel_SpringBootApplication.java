





import java.util.List;
import java.util.ArrayList;

public class PhotosMetaModel_SpringBootApplication  {






    private PhotosMetaModel_Spring photosmetamodel_spring;




    private List<PhotosMetaModel_Component> photosmetamodel_components;




    private List<PhotosMetaModel_Configuration> photosmetamodel_configurations;




    private List<PhotosMetaModel_Entity> photosmetamodel_entitys;


    public PhotosMetaModel_SpringBootApplication(
    ) {
        this.photosmetamodel_components = new ArrayList<>();
        this.photosmetamodel_configurations = new ArrayList<>();
        this.photosmetamodel_entitys = new ArrayList<>();
    }

    public PhotosMetaModel_SpringBootApplication(
        ArrayList<PhotosMetaModel_Component> photosmetamodel_components,        ArrayList<PhotosMetaModel_Configuration> photosmetamodel_configurations,        ArrayList<PhotosMetaModel_Entity> photosmetamodel_entitys    ) {
        this.photosmetamodel_components = photosmetamodel_components;
        this.photosmetamodel_configurations = photosmetamodel_configurations;
        this.photosmetamodel_entitys = photosmetamodel_entitys;
    }


    public PhotosMetaModel_Spring getPhotosmetamodel_spring() {
        return photosmetamodel_spring;
    }

    public void setPhotosmetamodel_spring(PhotosMetaModel_Spring photosmetamodel_spring) {
        this.photosmetamodel_spring = photosmetamodel_spring;
    }
    public List<PhotosMetaModel_Component> getPhotosmetamodel_components() {
        return photosmetamodel_components;
    }

    public void addPhotosmetamodel_component(Photosmetamodel_component photosmetamodel_component) {
        this.photosmetamodel_components.add(photosmetamodel_component);
    }
    public List<PhotosMetaModel_Configuration> getPhotosmetamodel_configurations() {
        return photosmetamodel_configurations;
    }

    public void addPhotosmetamodel_configuration(Photosmetamodel_configuration photosmetamodel_configuration) {
        this.photosmetamodel_configurations.add(photosmetamodel_configuration);
    }
    public List<PhotosMetaModel_Entity> getPhotosmetamodel_entitys() {
        return photosmetamodel_entitys;
    }

    public void addPhotosmetamodel_entity(Photosmetamodel_entity photosmetamodel_entity) {
        this.photosmetamodel_entitys.add(photosmetamodel_entity);
    }

}