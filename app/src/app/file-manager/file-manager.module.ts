/*
* DATAGERRY - OpenSource Enterprise CMDB
* Copyright (C) 2019 NETHINKS GmbH
*
* This program is free software: you can redistribute it and/or modify
* it under the terms of the GNU Affero General Public License as
* published by the Free Software Foundation, either version 3 of the
* License, or (at your option) any later version.
*
* This program is distributed in the hope that it will be useful,
* but WITHOUT ANY WARRANTY; without even the implied warranty of
* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
* GNU Affero General Public License for more details.

* You should have received a copy of the GNU Affero General Public License
* along with this program.  If not, see <https://www.gnu.org/licenses/>.
*/

import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { LayoutModule } from '../layout/layout.module';
import { FileManagerComponent } from './file-manager.component';
import { FileManagerRoutingModule } from './file-manager-routing.module';
import { TypeService } from '../framework/services/type.service';
import { ObjectService } from '../framework/services/object.service';
import { FolderTreeComponent } from './components/folder-tree/folder-tree.component';
import { FolderNodeComponent } from './components/folder-node/folder-node.component';
import { FileViewListComponent } from './components/file-view-list/file-view-list.component';
import { NewFolderDialogComponent } from './modal/new-folder-dialog/new-folder-dialog.component';
import { RenameDialogComponent } from './modal/rename-dialog/rename-dialog.component';
import { ReactiveFormsModule } from '@angular/forms';

@NgModule({
  entryComponents: [
    NewFolderDialogComponent,
    RenameDialogComponent
  ],
  declarations: [
    FileManagerComponent,
    FolderTreeComponent,
    FolderNodeComponent,
    FileViewListComponent,
    NewFolderDialogComponent,
    RenameDialogComponent,
  ],
  imports: [
    CommonModule,
    LayoutModule,
    FileManagerRoutingModule,
    ReactiveFormsModule
  ],
  providers: [
    TypeService,
    ObjectService
  ]
})
export class FileManagerModule { }
