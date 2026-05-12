





import java.util.List;
import java.util.ArrayList;

public class build_runtime_BuildRuntime  {






    private List<ResolverExtension> resolverextensions;




    private List<MetaDataTranslatorFactoryExtension> metadatatranslatorfactoryextensions;


    public build_runtime_BuildRuntime(
    ) {
        this.resolverextensions = new ArrayList<>();
        this.metadatatranslatorfactoryextensions = new ArrayList<>();
    }

    public build_runtime_BuildRuntime(
        ArrayList<ResolverExtension> resolverextensions,        ArrayList<MetaDataTranslatorFactoryExtension> metadatatranslatorfactoryextensions    ) {
        this.resolverextensions = resolverextensions;
        this.metadatatranslatorfactoryextensions = metadatatranslatorfactoryextensions;
    }


    public List<ResolverExtension> getResolverextensions() {
        return resolverextensions;
    }

    public void addResolverextension(Resolverextension resolverextension) {
        this.resolverextensions.add(resolverextension);
    }
    public List<MetaDataTranslatorFactoryExtension> getMetadatatranslatorfactoryextensions() {
        return metadatatranslatorfactoryextensions;
    }

    public void addMetadatatranslatorfactoryextension(Metadatatranslatorfactoryextension metadatatranslatorfactoryextension) {
        this.metadatatranslatorfactoryextensions.add(metadatatranslatorfactoryextension);
    }

}