





import java.util.List;
import java.util.ArrayList;

public class TypeReference  {






    private classifiers_Implementor classifiers_implementor;




    private generics_ExtendsTypeArgument generics_extendstypeargument;




    private generics_SuperTypeArgument generics_supertypeargument;




    private types_TypedElement types_typedelement;




    private generics_TypeParameter generics_typeparameter;


    public TypeReference(
    ) {
    }



    public classifiers_Implementor getClassifiers_implementor() {
        return classifiers_implementor;
    }

    public void setClassifiers_implementor(classifiers_Implementor classifiers_implementor) {
        this.classifiers_implementor = classifiers_implementor;
    }
    public generics_ExtendsTypeArgument getGenerics_extendstypeargument() {
        return generics_extendstypeargument;
    }

    public void setGenerics_extendstypeargument(generics_ExtendsTypeArgument generics_extendstypeargument) {
        this.generics_extendstypeargument = generics_extendstypeargument;
    }
    public generics_SuperTypeArgument getGenerics_supertypeargument() {
        return generics_supertypeargument;
    }

    public void setGenerics_supertypeargument(generics_SuperTypeArgument generics_supertypeargument) {
        this.generics_supertypeargument = generics_supertypeargument;
    }
    public types_TypedElement getTypes_typedelement() {
        return types_typedelement;
    }

    public void setTypes_typedelement(types_TypedElement types_typedelement) {
        this.types_typedelement = types_typedelement;
    }
    public generics_TypeParameter getGenerics_typeparameter() {
        return generics_typeparameter;
    }

    public void setGenerics_typeparameter(generics_TypeParameter generics_typeparameter) {
        this.generics_typeparameter = generics_typeparameter;
    }

}