





import java.util.List;
import java.util.ArrayList;

public class model_datasources_DataSourceLibraryConfiguration  {

    private String format;
    private String modelInterpreterId;





    private datasources_model_GeppettoLibrary datasources_model_geppettolibrary;


    public model_datasources_DataSourceLibraryConfiguration(
        String format,        String modelInterpreterId    ) {
        this.format = format;
        this.modelInterpreterId = modelInterpreterId;
    }


    public String getFormat() {
        return format;
    }

    public void setFormat(String format) {
        this.format = format;
    }
    public String getModelinterpreterid() {
        return modelInterpreterId;
    }

    public void setModelinterpreterid(String modelInterpreterId) {
        this.modelInterpreterId = modelInterpreterId;
    }

    public datasources_model_GeppettoLibrary getDatasources_model_geppettolibrary() {
        return datasources_model_geppettolibrary;
    }

    public void setDatasources_model_geppettolibrary(datasources_model_GeppettoLibrary datasources_model_geppettolibrary) {
        this.datasources_model_geppettolibrary = datasources_model_geppettolibrary;
    }

}