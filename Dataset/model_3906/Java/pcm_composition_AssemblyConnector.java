





import java.util.List;
import java.util.ArrayList;

public class pcm_composition_AssemblyConnector extends entity_Entity, connectors_Connector {






    private composition_AssemblyContext composition_assemblycontext;




    private RequiredRole requiredrole;




    private composition_AssemblyContext composition_assemblycontext;




    private composition_ComposedStructure composition_composedstructure;




    private ProvidedRole providedrole;


    public pcm_composition_AssemblyConnector(
    ) {
        super(
        );
    }



    public composition_AssemblyContext getComposition_assemblycontext() {
        return composition_assemblycontext;
    }

    public void setComposition_assemblycontext(composition_AssemblyContext composition_assemblycontext) {
        this.composition_assemblycontext = composition_assemblycontext;
    }
    public RequiredRole getRequiredrole() {
        return requiredrole;
    }

    public void setRequiredrole(RequiredRole requiredrole) {
        this.requiredrole = requiredrole;
    }
    public composition_AssemblyContext getComposition_assemblycontext() {
        return composition_assemblycontext;
    }

    public void setComposition_assemblycontext(composition_AssemblyContext composition_assemblycontext) {
        this.composition_assemblycontext = composition_assemblycontext;
    }
    public composition_ComposedStructure getComposition_composedstructure() {
        return composition_composedstructure;
    }

    public void setComposition_composedstructure(composition_ComposedStructure composition_composedstructure) {
        this.composition_composedstructure = composition_composedstructure;
    }
    public ProvidedRole getProvidedrole() {
        return providedrole;
    }

    public void setProvidedrole(ProvidedRole providedrole) {
        this.providedrole = providedrole;
    }

}