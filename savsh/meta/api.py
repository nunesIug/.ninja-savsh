from ninja import Router
from django.shortcuts import get_object_or_404
from typing import List
from ..schemas.MetaSchema import MetaSchema
from ..models import Meta

router = Router()

@router.get("/all", response=List[MetaSchema])
def Get_Metas(request):

    metas = Meta.objects.all()

    return metas
    

@router.get("/get-specific/{int:id}", response=MetaSchema)
def Get_Specific(request, id: int):

    meta = get_object_or_404(Meta, id=id)

    return meta


@router.post("/create-meta", response=MetaSchema)
def Create_Meta(request, body: MetaSchema):

    meta = Meta.objects.create(**body.dict())

    return meta


@router.put("/update/{int:id}", response=MetaSchema)
def Update_Meta(request, id: int, body: MetaSchema):

    meta = get_object_or_404(Meta, id=id)

    for attr, value in body.dict().items():
        setattr(meta, attr, value)

    meta.save()

    return meta


@router.delete("/delete/{int:id}")
def Delete_Meta(request, id: int):
    
    meta = get_object_or_404(Meta, id=id)
    meta.delete()

    return { "Meta deleted": True }